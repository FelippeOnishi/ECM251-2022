public class Tesoura extends Jogada {

    public Tesoura() {
        super(EnumJogadas.PAPEL, EnumJogadas.LAGARTO);
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.TESOURA;
    }

    @Override
    public String toString() {
        return String.join("\n",
        "                     .......                    ",
        "                  :--::::::---:                 ",
        "              .::::...........:::.              ",
        "             ::..................:-.            ",
        "           .-:............-.=......::.          ",
        "          ::.............:  .........::         ",
        "         -:.............::  =.........::        ",
        "        ::.............::  .:..........::       ",
        "       ::..............-   .............::      ",
        "      ::..............:.   -.............:.     ",
        "     .:...............-   -...............-     ",
        "     :...............=    =.........:::...::    ",
        "    ::..............:.   -........::.  :...:.   ",
        "    -...............:    :......:-.    -....:   ",
        "   .:...............:   .:....:-.     =:....:   ",
        "   :...............-    .:...-.     .-......:.  ",
        "   :..............::    -..::     .:-........-  ",
        "   :.............::     =.+      .=..........-  ",
        "  ::.............:      .:      ::...........:. ",
        "  -.............:.             =..............: ",
        "  -............::           .:-...............: ",
        "  -............-           :-.................: ",
        "  -...........=            =..................: ",
        "  -..........:               -:...............: ",
        "  -.........::                ................: ",
        "  -........::                 ................: ",
        "  ::.......:                =.:..............:. ",
        "  .:......-                  =...............-  ",
        "   :.....:.                  .:..............-  ",
        "   :....:.                   .:.............::  ",
        "   .:..=:                   :-:.............:   ",
        "    -:-                    ==...............:   ",
        "    -.                    -:...............:.   ",
        "     .                   -.................-    ",
        "     .                  -:................-     ",
        "      .               .:.................::     ",
        "    ..:.             .-.................::.:.   ",
        "  .:-:  .           ::.................::   ::  ",
        "  .--   ..        .=...................:      -.",
        " .::.     .    .-::..................::        .",
        "..         :  +.....................-.          ",
        ".           .-:...................::            ",
        "              .--..............:-:              ",
        "                .:-::::::::::::-.               ",
        "                 .. .........  ::               ",
        " ");
    }
      
}
