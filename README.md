NeoTrellisM4




    Merlin Functionality
        4 x 8 Board


        Show Menu Screen
            Lights Out
            Tic Tac Toe
            Memory
            Sequencer


        Lights Out

            Continue = true

            While Continue:

                Create Random Board
                    Generate 4 Random 8 bit numbers or 2 random 16 bit numbers
                    Bit 0 is 0,0 - Bit 1 is 0,1 - Bit 2 is 0,2 
                    For x = 0 to 8
                        For y = 0 to 4
                            BitPos = x + ( y * 8)
                            Value = bit at BitPos

                Won = false
                While !Won
                    Get Key Press
                        X, Y
                    Update Board
                        Toggle X, Y
                        Toggle X-1, Y
                        Toggle X+1, Y
                        Toggle X, Y-1
                        Toggle X, Y+1
                    Won = All LEDs On or Off
                        Count = Number of LEDS on
                        if Count = 0 or Count = Width * Height

                Do Win Sequence
                    Wait on Keypress

                Show Continue Screen
                    Wait on Keypress
                        Green = continue = true
                        Red = continue = stop



        Tic Tac Toe