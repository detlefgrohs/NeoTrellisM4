

#$COM = [System.IO.Ports.SerialPort]::getportnames()

#function read-com {
    $port= new-Object System.IO.Ports.SerialPort COM5,115200,None,8,one
    $port.Open()
    $port.DtrEnable = $true

    #Start-Sleep 2 # wait 2 seconds until Arduino is ready


    do {
        $line = $port.ReadLine()
        Write-Host $line # Do stuff here
    }
    while ($port.IsOpen)
#}
