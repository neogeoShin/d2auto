import win32con
import ctypes
import ctypes.wintypes as win

user32 = ctypes.WinDLL('user32', use_last_error=True)

class MsStructuer(ctypes.Structure):
    _fields_ = [('point', win.POINT),
                ('mouseDate', win.DWORD),
                ('flags', win.DWORD),
                ('time', win.DWORD),
                ('dwExtraInfo', ctypes.c_ulong)]

class KeyLogger:
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None

    def installHookProc(self,pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(win32con.WH_MOUSE_LL, pointer, None, 0)
        if not self.hooked:
            return False
        return True
    
    def uninstalHookProc(self):
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

def hookProc(nCode, wParam, lParam):
    if nCode == win32con.HC_ACTION and wParam == win32con.WM_LBUTTONDOWN:
        ms = MsStructuer.from_address(lParam)
        print(f'{ms.time}:{ms.point.x}, {ms.point.y}')#timeはミリ秒単位かな
    if nCode == win32con.HC_ACTION and wParam == win32con.WM_RBUTTONDOWN:
        print('右クリックが押されました。フックを解除します')
        kl.uninstalHookProc()
        return user32.CallNextHookEx(0, nCode, win.WPARAM(wParam), win.LPARAM(lParam))
    return user32.CallNextHookEx(0, nCode, win.WPARAM(wParam), win.LPARAM(lParam))

HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, win.WPARAM, win.LPARAM)
callback = HOOKPROC(hookProc)

kl = KeyLogger()
bool = kl.installHookProc(callback)
msg = win.MSG()
user32.GetMessageA(ctypes.byref(msg), 0, 0, 0)
