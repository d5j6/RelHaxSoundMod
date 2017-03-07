# Embedded file name: scripts/common/Lib/distutils/core.py
"""distutils.core

The only module that needs to be imported to use the Distutils; provides
the 'setup' function (which is to be called from the setup script).  Also
indirectly provides the Distribution and Command classes, although they are
really defined in distutils.dist and distutils.cmd.
"""
__revision__ = '$Id$'
import sys
import os
from distutils.debug import DEBUG
from distutils.errors import DistutilsSetupError, DistutilsArgError, DistutilsError, CCompilerError
from distutils.dist import Distribution
from distutils.cmd import Command
from distutils.config import PyPIRCCommand
from distutils.extension import Extension
USAGE = 'usage: %(script)s [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]\n   or: %(script)s --help [cmd1 cmd2 ...]\n   or: %(script)s --help-commands\n   or: %(script)s cmd --help\n'

def gen_usage(script_name):
    script = os.path.basename(script_name)
    return USAGE % {'script': script}


_setup_stop_after = None
_setup_distribution = None
setup_keywords = ('distclass', 'script_name', 'script_args', 'options', 'name', 'version', 'author', 'author_email', 'maintainer', 'maintainer_email', 'url', 'license', 'description', 'long_description', 'keywords', 'platforms', 'classifiers', 'download_url', 'requires', 'provides', 'obsoletes')
extension_keywords = ('name', 'sources', 'include_dirs', 'define_macros', 'undef_macros', 'library_dirs', 'libraries', 'runtime_library_dirs', 'extra_objects', 'extra_compile_args', 'extra_link_args', 'swig_opts', 'export_symbols', 'depends', 'language')

def setup(**attrs):
    """The gateway to the Distutils: do everything your setup script needs
    to do, in a highly flexible and user-driven way.  Briefly: create a
    Distribution instance; find and parse config files; parse the command
    line; run each Distutils command found there, customized by the options
    supplied to 'setup()' (as keyword arguments), in config files, and on
    the command line.
    
    The Distribution instance might be an instance of a class supplied via
    the 'distclass' keyword argument to 'setup'; if no such class is
    supplied, then the Distribution class (in dist.py) is instantiated.
    All other arguments to 'setup' (except for 'cmdclass') are used to set
    attributes of the Distribution instance.
    
    The 'cmdclass' argument, if supplied, is a dictionary mapping command
    names to command classes.  Each command encountered on the command line
    will be turned into a command class, which is in turn instantiated; any
    class found in 'cmdclass' is used in place of the default, which is
    (for command 'foo_bar') class 'foo_bar' in module
    'distutils.command.foo_bar'.  The command class must provide a
    'user_options' attribute which is a list of option specifiers for
    'distutils.fancy_getopt'.  Any command-line options between the current
    and the next command are used to set attributes of the current command
    object.
    
    When the entire command-line has been successfully parsed, calls the
    'run()' method on each command object in turn.  This method will be
    driven entirely by the Distribution object (which each command object
    has a reference to, thanks to its constructor), and the
    command-specific options that became attributes of each command
    object.
    """
    global _setup_stop_after
    global _setup_distribution
    klass = attrs.get('distclass')
    if klass:
        del attrs['distclass']
    else:
        klass = Distribution
    if 'script_name' not in attrs:
        attrs['script_name'] = os.path.basename(sys.argv[0])
    if 'script_args' not in attrs:
        attrs['script_args'] = sys.argv[1:]
    try:
        _setup_distribution = dist = klass(attrs)
    except DistutilsSetupError as msg:
        if 'name' in attrs:
            raise SystemExit, 'error in %s setup command: %s' % (attrs['name'], msg)
        else:
            raise SystemExit, 'error in setup command: %s' % msg

    if _setup_stop_after == 'init':
        return dist
    dist.parse_config_files()
    if DEBUG:
        print 'options (after parsing config files):'
        dist.dump_option_dicts()
    if _setup_stop_after == 'config':
        return dist
    try:
        ok = dist.parse_command_line()
    except DistutilsArgError as msg:
        raise SystemExit, gen_usage(dist.script_name) + '\nerror: %s' % msg

    if DEBUG:
        print 'options (after parsing command line):'
        dist.dump_option_dicts()
    if _setup_stop_after == 'commandline':
        return dist
    if ok:
        try:
            dist.run_commands()
        except KeyboardInterrupt:
            raise SystemExit, 'interrupted'
        except (IOError, os.error) as exc:
            if DEBUG:
                sys.stderr.write('error: %s\n' % (exc,))
                raise
            else:
                raise SystemExit, 'error: %s' % (exc,)
        except (DistutilsError, CCompilerError) as msg:
            if DEBUG:
                raise
            else:
                raise SystemExit, 'error: ' + str(msg)

    return dist


def run_setup(script_name, script_args = None, stop_after = 'run'):
    """Run a setup script in a somewhat controlled environment, and
    return the Distribution instance that drives things.  This is useful
    if you need to find out the distribution meta-data (passed as
    keyword args from 'script' to 'setup()', or the contents of the
    config files or command-line.
    
    'script_name' is a file that will be run with 'execfile()';
    'sys.argv[0]' will be replaced with 'script' for the duration of the
    call.  'script_args' is a list of strings; if supplied,
    'sys.argv[1:]' will be replaced by 'script_args' for the duration of
    the call.
    
    'stop_after' tells 'setup()' when to stop processing; possible
    values:
      init
        stop after the Distribution instance has been created and
        populated with the keyword arguments to 'setup()'
      config
        stop after config files have been parsed (and their data
        stored in the Distribution instance)
      commandline
        stop after the command-line ('sys.argv[1:]' or 'script_args')
        have been parsed (and the data stored in the Distribution)
      run [default]
        stop after all commands have been run (the same as if 'setup()'
        had been called in the usual way
    
    Returns the Distribution instance, which provides all information
    used to drive the Distutils.
    """
    global _setup_stop_after
    if stop_after not in ('init', 'config', 'commandline', 'run'):
        raise ValueError, "invalid value for 'stop_after': %r" % (stop_after,)
    _setup_stop_after = stop_after
    save_argv = sys.argv
    g = {'__file__': script_name}
    l = {}
    try:
        try:
            sys.argv[0] = script_name
            if script_args is not None:
                sys.argv[1:] = script_args
            f = open(script_name)
            try:
                exec f.read() in g, l
            finally:
                f.close()

        finally:
            sys.argv = save_argv
            _setup_stop_after = None

    except SystemExit:
        pass
    except:
        raise

    if _setup_distribution is None:
        raise RuntimeError, "'distutils.core.setup()' was never called -- perhaps '%s' is not a Distutils setup script?" % script_name
    return _setup_distribution
