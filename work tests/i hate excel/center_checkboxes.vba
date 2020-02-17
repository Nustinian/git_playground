Sub Center_Checkboxes()
    Dim xRg As Range
    Dim chkBox As OLEObject
    Dim chkFBox As CheckBox
    On Error Resume Next
    Application.ScreenUpdating = False
    For Each chkBox In ActiveSheet.OLEObjects
        If TypeName(chkBox.Object) = "CheckBox" Then
            Set xRg = chkBox.TopLeftCell
            chkBox.Width = xRg.Width
            chkBox.Height = xRg.Height
            chkBox.Left = xRg.Left + (xRg.Width - chkBox.Width / 2)
            chkBox.Top = xRg.Top + (xRg.Height - chkBox.Height / 2)
        End If
    Next
    For Each chkFBox In ActiveSheet.CheckBoxes
        Set xRg = chkFBox.TopLeftCell
        chkFBox.Width = xRg.Width
        chkFBox.Height = xRg.Height
        chkFBox.Left = xRg.Left + (xRg.Width - chkFBox.Width) / 2
        chkFBox.Top = xRg.Top + (xRg.Height - chkFBox.Height) / 2
    Next
    Application.ScreenUpdating = True
End Sub
