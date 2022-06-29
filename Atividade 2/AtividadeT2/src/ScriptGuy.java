public class ScriptGuy extends Membro{

    public ScriptGuy(String userName, String email, EnumFuncao funcao, EnumHorarios horario) {
        super(userName, email, funcao, horario);
        setRegularMessage(regularMessage);
        setExtraMessage(extraMessage);
    }

    private final String regularMessage = "Prazer em ajudar novos amigos de codigo!";
    private final String extraMessage = "QU3Ro_S3us_r3curs0s.py";
}
