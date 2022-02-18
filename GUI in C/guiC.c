#include<windows.h>
// #include<windowsx.h>
// CALLBACK is the calling convention
LRESULT CALLBACK WindowProcedure(HWND, UINT, WPARAM, LPARAM);

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
        case WM_DESTROY:
            PostQuitMessage(0);
            break;
        default:
            return DefWindowProcW(hWnd, msg, wp, lp);
    }
}