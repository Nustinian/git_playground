Sub Jump_Yellow_Timestamp()
Dim xChk As CheckBox
Set xChk = ActiveSheet.CheckBoxes(Application.Caller)
With xChk.TopLeftCell.Offset(, -3)
    If xChk.Value = xlOff Then
        .Value = ""
    Else
       .Value = Time
    End If
End With
With xChk.TopLeftCell.Offset(2, -6)
    If xChk.Value = xlOff Then
        .Value = ""
    Else
       .Value = Time
    End If
End With
End Sub

