#include<windows.h>
// In this menus are created over the header file
// #include<windowsx.h>

#define FILE_MENU_NEW 1
#define FILE_MENU_OPEN 2
#define FILE_MENU_EXIT 3
// CALLBACK is the calling convention
LRESULT CALLBACK WindowProcedure(HWND, UINT, WPARAM, LPARAM);

void AddMenus(HWND);

HMENU hMenu;

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR IpCmdLine, int nCmdShow)
{
    /*
    HINSTANCE : IDE of the operating system, use this while creating window
    LPSTR : it is the typedef for the characters
    */
    // MessageBox(NULL, "WELCOME TO THE DIGITAL-LIBRARY", "Mera Beta", MB_OK);

    // to create a window class

    WNDCLASSW wc = {0};
    wc.hbrBackground = (HBRUSH)COLOR_WINDOW;
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hInstance = hInstance;
    wc.lpszClassName = L"myWindowClass"; // this is the basic identifier for our class
    wc.lpfnWndProc = WindowProcedure;// this is the window procedure

    if(!RegisterClassW(&wc))
    {
        return -1;
    }
    CreateWindowW(L"myWindowClass", L"My Window", WS_OVERLAPPEDWINDOW | WS_VISIBLE, 100, 100, 500, 500, NULL, NULL, NULL, NULL);
    
    // this is the message loop
    MSG msg = {0};
    while(GetMessage((&msg), NULL, NULL, NULL))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}



LRESULT CALLBACK WindowProcedure(HWND hWnd, UINT msg, WPARAM wp, LPARAM lp)
{
    switch(msg)
    {
        case WM_COMMAND:
            switch(wp)
            {
                case FILE_MENU_EXIT:
                    DestroyWindow(hWnd);
                    break;
                case FILE_MENU_NEW:
                    MessageBeep(MB_ICONINFORMATION);
                    break;
                case FILE_MENU_OPEN:

                    break;
            }
            break;
        case WM_CREATE:
            AddMenus(hWnd);
            break;
        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProcW(hWnd, msg, wp, lp);
    }
}

void AddMenus(HWND hWnd)
{
    hMenu = CreateMenu();

    // this will open another menu --> submenu
    HMENU hSubMenu = CreateMenu();

    AppendMenu(hSubMenu, MF_STRING, NULL, "SubMenu Iton");

    // this is for drop-down menu
    HMENU hFileMenu = CreateMenu();

    AppendMenu(hFileMenu, MF_STRING, FILE_MENU_NEW, "New File");
    AppendMenu(hFileMenu, MF_POPUP, (UINT_PTR)hSubMenu, "Open SubMenu");
    
    // MF_SEPERATOR creates the line
    AppendMenu(hFileMenu, MF_SEPARATOR, NULL, NULL);

    AppendMenu(hFileMenu, MF_STRING, FILE_MENU_EXIT, "Exit");
    AppendMenu(hFileMenu, MF_STRING, FILE_MENU_NEW, "Save As");


    AppendMenu(hMenu, MF_POPUP, (UINT_PTR)hFileMenu, "File");
    AppendMenu(hMenu, MF_STRING, NULL, "Help");

    SetMenu(hWnd, hMenu);
}