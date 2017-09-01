;Reccomended Setup
  #NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
  ; #W arn  ; Enable warnings to assist with detecting common errors.
  SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
  SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

SetTitleMatchMode, 2                                                            ;;Lets active window match anything with title, not a specific title
#ifWinActive Script

;setup if and with
:*:if::
    Send, if(){{}{}}
    Send, {Left}{Enter}{Enter}{Up}{tab}{Up}{End}{Left}{Left}
    Return
:*:with::
    Send, with(){{}{}}
    Send, {Left}{Enter}{Enter}{Up}{tab}{Up}{End}{Left}{Left}
    Return

;add end to up and down
^Down::
    Send, {Down}{End}
    Return
^Up::
    Send, {Up}{End}
    Return

;shorthand
~o & b::
    Send, {Backspace}
    Send, obj_
    Return
~s & p::
    Send, {Backspace}
    Send, spr_
    Return
~m & x::
    Send, {Backspace}
    Send, mouse_x
    Return
~m & y::
    Send, {Backspace}
    Send, mouse_y
    Return
