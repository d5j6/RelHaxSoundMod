# Embedded file name: scripts/common/Lib/plat-irix6/FILE.py
from warnings import warnpy3k
warnpy3k('the FILE module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
_MIPS_ISA_MIPS1 = 1
_MIPS_ISA_MIPS2 = 2
_MIPS_ISA_MIPS3 = 3
_MIPS_ISA_MIPS4 = 4
_MIPS_SIM_ABI32 = 1
_MIPS_SIM_NABI32 = 2
_MIPS_SIM_ABI64 = 3
P_MYID = -1
P_MYHOSTID = -1
ONBITSMAJOR = 7
ONBITSMINOR = 8
OMAXMAJ = 127
OMAXMIN = 255
NBITSMAJOR = 14
NBITSMINOR = 18
MAXMAJ = 511
MAXMIN = 262143
OLDDEV = 0
NEWDEV = 1
MKDEV_VER = NEWDEV

def IS_STRING_SPEC_DEV(x):
    return dev_t(x) == __makedev(MKDEV_VER, 0, 0)


def major(dev):
    return __major(MKDEV_VER, dev)


def minor(dev):
    return __minor(MKDEV_VER, dev)


FD_SETSIZE = 1024
__NBBY = 8
NULL = 0L
NBBY = 8
MAXCPU = 128

def CPUMASK_INDEX(bit):
    return bit >> 6


def CPUMASK_SHFT(bit):
    return bit & 63


def CPUMASK_IS_ZERO(p):
    return p == 0


def CPUMASK_IS_NONZERO(p):
    return p != 0


def CNODEMASK_IS_ZERO(p):
    return p == 0


def CNODEMASK_IS_NONZERO(p):
    return p != 0


SIGHUP = 1
SIGINT = 2
SIGQUIT = 3
SIGILL = 4
SIGTRAP = 5
SIGIOT = 6
SIGABRT = 6
SIGEMT = 7
SIGFPE = 8
SIGKILL = 9
SIGBUS = 10
SIGSEGV = 11
SIGSYS = 12
SIGPIPE = 13
SIGALRM = 14
SIGTERM = 15
SIGUSR1 = 16
SIGUSR2 = 17
SIGCLD = 18
SIGCHLD = 18
SIGPWR = 19
SIGWINCH = 20
SIGURG = 21
SIGPOLL = 22
SIGIO = 22
SIGSTOP = 23
SIGTSTP = 24
SIGCONT = 25
SIGTTIN = 26
SIGTTOU = 27
SIGVTALRM = 28
SIGPROF = 29
SIGXCPU = 30
SIGXFSZ = 31
SIGK32 = 32
SIGCKPT = 33
SIGRESTART = 34
SIGUME = 35
SIGPTINTR = 47
SIGPTRESCHED = 48
SIGRTMIN = 49
SIGRTMAX = 64
__sigargs = int
SIGEV_NONE = 128
SIGEV_SIGNAL = 129
SIGEV_CALLBACK = 130
SIGEV_THREAD = 131
SI_MAXSZ = 128
SI_USER = 0
SI_KILL = SI_USER
SI_QUEUE = -1
SI_ASYNCIO = -2
SI_TIMER = -3
SI_MESGQ = -4
ILL_ILLOPC = 1
ILL_ILLOPN = 2
ILL_ILLADR = 3
ILL_ILLTRP = 4
ILL_PRVOPC = 5
ILL_PRVREG = 6
ILL_COPROC = 7
ILL_BADSTK = 8
NSIGILL = 8
FPE_INTDIV = 1
FPE_INTOVF = 2
FPE_FLTDIV = 3
FPE_FLTOVF = 4
FPE_FLTUND = 5
FPE_FLTRES = 6
FPE_FLTINV = 7
FPE_FLTSUB = 8
NSIGFPE = 8
SEGV_MAPERR = 1
SEGV_ACCERR = 2
NSIGSEGV = 2
BUS_ADRALN = 1
BUS_ADRERR = 2
BUS_OBJERR = 3
NSIGBUS = 3
TRAP_BRKPT = 1
TRAP_TRACE = 2
NSIGTRAP = 2
CLD_EXITED = 1
CLD_KILLED = 2
CLD_DUMPED = 3
CLD_TRAPPED = 4
CLD_STOPPED = 5
CLD_CONTINUED = 6
NSIGCLD = 6
POLL_IN = 1
POLL_OUT = 2
POLL_MSG = 3
POLL_ERR = 4
POLL_PRI = 5
POLL_HUP = 6
NSIGPOLL = 6
UME_ECCERR = 1
NSIGUME = 1
SIG_NOP = 0
SIG_BLOCK = 1
SIG_UNBLOCK = 2
SIG_SETMASK = 3
SIG_SETMASK32 = 256
SA_ONSTACK = 1
SA_RESETHAND = 2
SA_RESTART = 4
SA_SIGINFO = 8
SA_NODEFER = 16
SA_NOCLDWAIT = 65536
SA_NOCLDSTOP = 131072
_SA_BSDCALL = 268435456
MINSIGSTKSZ = 512
SIGSTKSZ = 8192
SS_ONSTACK = 1
SS_DISABLE = 2
NGREG = 36
NGREG = 37
GETCONTEXT = 0
SETCONTEXT = 1
UC_SIGMASK = 1
UC_STACK = 2
UC_CPU = 4
UC_MAU = 8
UC_MCONTEXT = UC_CPU | UC_MAU
UC_ALL = UC_SIGMASK | UC_STACK | UC_MCONTEXT
CTX_R0 = 0
CTX_AT = 1
CTX_V0 = 2
CTX_V1 = 3
CTX_A0 = 4
CTX_A1 = 5
CTX_A2 = 6
CTX_A3 = 7
CTX_T0 = 8
CTX_T1 = 9
CTX_T2 = 10
CTX_T3 = 11
CTX_T4 = 12
CTX_T5 = 13
CTX_T6 = 14
CTX_T7 = 15
CTX_A4 = 8
CTX_A5 = 9
CTX_A6 = 10
CTX_A7 = 11
CTX_T0 = 12
CTX_T1 = 13
CTX_T2 = 14
CTX_T3 = 15
CTX_S0 = 16
CTX_S1 = 17
CTX_S2 = 18
CTX_S3 = 19
CTX_S4 = 20
CTX_S5 = 21
CTX_S6 = 22
CTX_S7 = 23
CTX_T8 = 24
CTX_T9 = 25
CTX_K0 = 26
CTX_K1 = 27
CTX_GP = 28
CTX_SP = 29
CTX_S8 = 30
CTX_RA = 31
CTX_MDLO = 32
CTX_MDHI = 33
CTX_CAUSE = 34
CTX_EPC = 35
CTX_SR = 36
CXT_R0 = CTX_R0
CXT_AT = CTX_AT
CXT_V0 = CTX_V0
CXT_V1 = CTX_V1
CXT_A0 = CTX_A0
CXT_A1 = CTX_A1
CXT_A2 = CTX_A2
CXT_A3 = CTX_A3
CXT_T0 = CTX_T0
CXT_T1 = CTX_T1
CXT_T2 = CTX_T2
CXT_T3 = CTX_T3
CXT_T4 = CTX_T4
CXT_T5 = CTX_T5
CXT_T6 = CTX_T6
CXT_T7 = CTX_T7
CXT_S0 = CTX_S0
CXT_S1 = CTX_S1
CXT_S2 = CTX_S2
CXT_S3 = CTX_S3
CXT_S4 = CTX_S4
CXT_S5 = CTX_S5
CXT_S6 = CTX_S6
CXT_S7 = CTX_S7
CXT_T8 = CTX_T8
CXT_T9 = CTX_T9
CXT_K0 = CTX_K0
CXT_K1 = CTX_K1
CXT_GP = CTX_GP
CXT_SP = CTX_SP
CXT_S8 = CTX_S8
CXT_RA = CTX_RA
CXT_MDLO = CTX_MDLO
CXT_MDHI = CTX_MDHI
CXT_CAUSE = CTX_CAUSE
CXT_EPC = CTX_EPC
CXT_SR = CTX_SR
CTX_FV0 = 0
CTX_FV1 = 2
CTX_FA0 = 12
CTX_FA1 = 13
CTX_FA2 = 14
CTX_FA3 = 15
CTX_FA4 = 16
CTX_FA5 = 17
CTX_FA6 = 18
CTX_FA7 = 19
CTX_FT0 = 4
CTX_FT1 = 5
CTX_FT2 = 6
CTX_FT3 = 7
CTX_FT4 = 8
CTX_FT5 = 9
CTX_FT6 = 10
CTX_FT7 = 11
CTX_FT8 = 20
CTX_FT9 = 21
CTX_FT10 = 22
CTX_FT11 = 23
CTX_FT12 = 1
CTX_FT13 = 3
CTX_FS0 = 24
CTX_FS1 = 25
CTX_FS2 = 26
CTX_FS3 = 27
CTX_FS4 = 28
CTX_FS5 = 29
CTX_FS6 = 30
CTX_FS7 = 31
CTX_FT8 = 21
CTX_FT9 = 23
CTX_FT10 = 25
CTX_FT11 = 27
CTX_FT12 = 29
CTX_FT13 = 31
CTX_FT14 = 1
CTX_FT15 = 3
CTX_FS0 = 20
CTX_FS1 = 22
CTX_FS2 = 24
CTX_FS3 = 26
CTX_FS4 = 28
CTX_FS5 = 30
SV_ONSTACK = 1
SV_INTERRUPT = 2
NUMBSDSIGS = 32

def sigmask(sig):
    return 1L << sig - 1


def sigmask(sig):
    return 1L << sig - 1


SIG_ERR = -1
SIG_IGN = 1
SIG_HOLD = 2
SIG_DFL = 0
NSIG = 65
MAXSIG = NSIG - 1
NUMSIGS = NSIG - 1
BRK_USERBP = 0
BRK_KERNELBP = 1
BRK_ABORT = 2
BRK_BD_TAKEN = 3
BRK_BD_NOTTAKEN = 4
BRK_SSTEPBP = 5
BRK_OVERFLOW = 6
BRK_DIVZERO = 7
BRK_RANGE = 8
BRK_PSEUDO_OP_BIT = 128
BRK_PSEUDO_OP_MAX = 3
BRK_CACHE_SYNC = 128
BRK_MULOVF = 1023
_POSIX_VERSION = 199506L
_POSIX_VERSION = 199506
_POSIX_VDISABLE = 0
MAX_INPUT = 512
MAX_CANON = 256
UID_NOBODY = 60001
GID_NOBODY = UID_NOBODY
UID_NOACCESS = 60002
MAXPID = 2147483632
MAXUID = 2147483647
MAXLINK = 30000
SSIZE = 1
SINCR = 1
KSTKSIZE = 1
EXTKSTKSIZE = 1
KSTKIDX = 0
KSTEIDX = 1
EXTKSTKSIZE = 0
KSTKIDX = 0
CANBSIZ = 256
HZ = 100
TICK = 10000000
NOFILE = 20
NGROUPS_UMIN = 0
NGROUPS_UMAX = 32
NGROUPS = 16
PMASK = 127
PCATCH = 256
PLTWAIT = 512
PRECALC = 512
PSWP = 0
PINOD = 10
PSNDD = PINOD
PRIBIO = 20
PZERO = 25
PMEM = 0
NZERO = 20
PPIPE = 26
PVFS = 27
PWAIT = 30
PSLEP = 39
PUSER = 60
PBATCH_CRITICAL = -1
PTIME_SHARE = -2
PTIME_SHARE_OVER = -3
PBATCH = -4
PWEIGHTLESS = -5
IO_NBPC = 4096
IO_BPCSHIFT = 12
MIN_NBPC = 4096
MIN_BPCSHIFT = 12
MIN_CPSSHIFT = 10
BPCSHIFT = 12
CPSSHIFT = 10
BPCSHIFT = 14
CPSSHIFT = 12
CPSSHIFT = 11
BPSSHIFT = BPCSHIFT + CPSSHIFT
NULL = 0L
CMASK = 18
NODEV = -1
NOPAGE = -1
NBPSCTR = 512
SCTRSHFT = 9

def BASEPRI(psw):
    return psw & SR_IMASK == SR_IMASK0


def BASEPRI(psw):
    return psw & SR_IMASK == SR_IMASK


def USERMODE(psw):
    return psw & SR_KSU_MSK == SR_KSU_USR


MAXPATHLEN = 1024
MAXSYMLINKS = 30
MAXNAMELEN = 256
PIPE_BUF = 10240
PIPE_MAX = 10240
NBBY = 8
BBSHIFT = 9
BBSIZE = 1 << BBSHIFT
BBMASK = BBSIZE - 1

def BBTOB(bbs):
    return bbs << BBSHIFT


def OFFTOBB(bytes):
    return __uint64_t(bytes) + BBSIZE - 1 >> BBSHIFT


def OFFTOBBT(bytes):
    return off_t(bytes) >> BBSHIFT


def BBTOOFF(bbs):
    return off_t(bbs) << BBSHIFT


SEEKLIMIT32 = 2147483647
MAXBSIZE = 8192
DEV_BSIZE = BBSIZE
DEV_BSHIFT = BBSHIFT

def btodb(bytes):
    pass


def dbtob(db):
    pass


BLKDEV_IOSHIFT = BPCSHIFT
BLKDEV_IOSIZE = 1 << BLKDEV_IOSHIFT

def BLKDEV_OFF(off):
    return off & BLKDEV_IOSIZE - 1


def BLKDEV_LBN(off):
    return off >> BLKDEV_IOSHIFT


def BLKDEV_LTOP(bn):
    return bn * BLKDEV_BB


MAXHOSTNAMELEN = 256

def DELAY(n):
    return us_delay(n)


def DELAYBUS(n):
    return us_delaybus(n)


TIMEPOKE_NOW = -100L
MUTEX_DEFAULT = 0
METER_NAMSZ = 16
METER_NO_SEQ = -1

def mutex_spinlock(l):
    return splhi()


def mutex_spintrylock(l):
    return splhi()


def spinlock_initialized(l):
    return 1


SV_FIFO = 0
SV_LIFO = 2
SV_PRIO = 4
SV_KEYED = 6
SV_DEFAULT = SV_FIFO
SEMA_NOHIST = 1
SEMA_LOCK = 4
NSCHEDCLASS = -PWEIGHTLESS + 1
MR_ACCESS = 1
MR_UPDATE = 2
MRLOCK_BARRIER = 1
MRLOCK_BEHAVIOR = 2
MRLOCK_DBLTRIPPABLE = 4
MRLOCK_ALLOW_EQUAL_PRI = 8
MRLOCK_DEFAULT = MRLOCK_BARRIER

def mraccess(mrp):
    return mraccessf(mrp, 0)


def mrupdate(mrp):
    return mrupdatef(mrp, 0)


def mp_mutex_unlock(m):
    return mutex_unlock(m)


def mp_mutex_trylock(m):
    return mutex_trylock(m)


def mp_mutex_spinlock(m):
    return mutex_spinlock(m)


MON_LOCKED = 1
MON_WAITING = 2
MON_TIMEOUT = 4
MON_DOSRV = 8
MON_RUN = 16
MR_READER_BUCKETS = 13

def initlock(l):
    return spinlock_init(l, 0)


def ownlock(x):
    return 1


def mutex_enter(m):
    return mutex_lock(m, PZERO)


def mutex_tryenter(m):
    return mutex_trylock(m)


def mutex_exit(m):
    return mutex_unlock(m)


def cv_signal(cv):
    return sv_signal(cv)


def cv_broadcast(cv):
    return sv_broadcast(cv)


def cv_destroy(cv):
    return sv_destroy(cv)


RW_READER = MR_ACCESS
RW_WRITER = MR_UPDATE

def rw_exit(r):
    return mrunlock(r)


def rw_tryupgrade(r):
    return mrtrypromote(r)


def rw_downgrade(r):
    return mrdemote(r)


def rw_destroy(r):
    return mrfree(r)


def RW_WRITE_HELD(r):
    return ismrlocked(r, MR_UPDATE)


def RW_READ_HELD(r):
    return ismrlocked(r, MR_ACCESS)


MS_FREE = 0
MS_UPD = 1
MS_ACC = 2
MS_WAITERS = 4
FNDELAY = 4
FAPPEND = 8
FSYNC = 16
FDSYNC = 32
FRSYNC = 64
FNONBLOCK = 128
FASYNC = 4096
FLARGEFILE = 8192
FNONBLK = FNONBLOCK
FDIRECT = 32768
FBULK = 65536
FDIRENT64 = 32768
FCREAT = 256
FTRUNC = 512
FEXCL = 1024
FNOCTTY = 2048
O_RDONLY = 0
O_WRONLY = 1
O_RDWR = 2
O_NDELAY = 4
O_APPEND = 8
O_SYNC = 16
O_DSYNC = 32
O_RSYNC = 64
O_NONBLOCK = 128
O_LARGEFILE = 8192
O_DIRECT = 32768
O_BULK = 65536
O_CREAT = 256
O_TRUNC = 512
O_EXCL = 1024
O_NOCTTY = 2048
F_DUPFD = 0
F_GETFD = 1
F_SETFD = 2
F_GETFL = 3
F_SETFL = 4
F_SETLK = 6
F_SETLKW = 7
F_CHKFL = 8
F_ALLOCSP = 10
F_FREESP = 11
F_SETBSDLK = 12
F_SETBSDLKW = 13
F_GETLK = 14
F_CHKLK = 15
F_CHKLKW = 16
F_CLNLK = 17
F_RSETLK = 20
F_RGETLK = 21
F_RSETLKW = 22
F_GETOWN = 23
F_SETOWN = 24
F_DIOINFO = 30
F_FSGETXATTR = 31
F_FSSETXATTR = 32
F_GETLK64 = 33
F_SETLK64 = 34
F_SETLKW64 = 35
F_ALLOCSP64 = 36
F_FREESP64 = 37
F_GETBMAP = 38
F_FSSETDM = 39
F_RESVSP = 40
F_UNRESVSP = 41
F_RESVSP64 = 42
F_UNRESVSP64 = 43
F_GETBMAPA = 44
F_FSGETXATTRA = 45
F_SETBIOSIZE = 46
F_GETBIOSIZE = 47
F_GETOPS = 50
F_DMAPI = 51
F_FSYNC = 52
F_FSYNC64 = 53
F_GETBDSATTR = 54
F_SETBDSATTR = 55
F_GETBMAPX = 56
F_SETPRIO = 57
F_GETPRIO = 58
F_RDLCK = 1
F_WRLCK = 2
F_UNLCK = 3
O_ACCMODE = 3
FD_CLOEXEC = 1
FD_NODUP_FORK = 4
BMV_IF_ATTRFORK = 1
BMV_IF_NO_DMAPI_READ = 2
BMV_IF_PREALLOC = 4
BMV_IF_VALID = BMV_IF_ATTRFORK | BMV_IF_NO_DMAPI_READ | BMV_IF_PREALLOC
BMV_OF_PREALLOC = 1
BMV_IF_EXTENDED = 1073741824
FMASK = 102655
FOPEN = 4294967295L
FREAD = 1
FWRITE = 2
FNDELAY = 4
FAPPEND = 8
FSYNC = 16
FDSYNC = 32
FRSYNC = 64
FNONBLOCK = 128
FASYNC = 4096
FNONBLK = FNONBLOCK
FLARGEFILE = 8192
FDIRECT = 32768
FBULK = 65536
FCREAT = 256
FTRUNC = 512
FEXCL = 1024
FNOCTTY = 2048
FINVIS = 256
FSOCKET = 512
FINPROGRESS = 1024
FPRIORITY = 2048
FPRIO = 16384
FDIRENT64 = 32768
FCLOSEXEC = 1
LOCK_SH = 1
LOCK_EX = 2
LOCK_NB = 4
LOCK_UN = 8
L_SET = 0
L_INCR = 1
L_XTND = 2
F_OK = 0
X_OK = 1
W_OK = 2
R_OK = 4
