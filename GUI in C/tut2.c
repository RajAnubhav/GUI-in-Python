#include<windows.h>
#include<wchar.h>

/*
    NOTE: 
    Remember : We can't declare the variable in switch statement
*/

// In this menus are created over the header file
  
#define FILE_MENU_NEW 1
#define FILE_MENU_OPEN 2
#define FILE_MENU_EXIT 3
#define CHANGE_TITLE 4

// CALLBACK is the calling convention
LRESULT CALLBACK WindowProcedure(HWND, UINT, WPARAM, LPARAM);

void AddMenus(HWND);
void AddControls(HWND);

HMENU hMenu;
HWND hEdit;
wchar_t text[100];
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
                case CHANGE_TITLE:
                    GetWindowTextW(hEdit, text, 100);
                    SetWindowTextW(hWnd, text);
                    break;
            }
            break;
        case WM_CREATE:
            AddMenus(hWnd);
            AddControls(hWnd);
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

    AppendMenu(hSubMenu, MF_STRING, CHANGE_TITLE, "Change Title");

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

void AddControls(HWND hWnd)
{
    CreateWindowW(L"static", L"Enter text here: ", WS_VISIBLE | WS_CHILD | WS_BORDER | SS_CENTER, 200, 100, 100, 50, hWnd, NULL, NULL, NULL);
    hEdit = CreateWindowW(L"Edit", L"...", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_MULTILINE | ES_AUTOVSCROLL | ES_AUTOHSCROLL, 200, 152, 100, 50, hWnd, NULL, NULL, NULL);
}