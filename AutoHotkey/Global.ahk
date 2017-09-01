;Reccomended Setup
  #NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
  ; #Warn  ; Enable warnings to assist with detecting common errors.
  SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
  SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;Open programs with logitech g5 key
^+!g::
    Run, C:\Users\jared\GameMaker-Studio 1.4\GameMaker-Studio
    Return
^+!e::
    Run, excel
    Return
^+!c::
    Run, C:\Program Files (x86)\Google\Chrome\Application\chrome
    Return
^+!NumpadAdd::
    Run, notepad
    Return
;^+!w::
;    Run,


;window control
^WheelUp::
    WinMaximize, A                                                              ;maximize active window, a for active
    Return
^WheelDown::
    WinRestore, A
    Return
^+WheelDown::
    WinMinimize, A
    Return
^WheelRight::
    Send, #{Right}
    Return
^WheelLeft::
    Send, #{Left}
    Return
