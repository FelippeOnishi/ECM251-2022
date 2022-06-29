public class HeavyLift extends Membro{

    public HeavyLift(String userName, String email, EnumFuncao funcao, EnumHorarios horario) {
        super(userName, email, funcao, horario);
    setRegularMessage(regularMessage);
    setExtraMessage(extraMessage);
    }

    private final String regularMessage = "Podem contar conosco!";
    private final String extraMessage = "N00b_qu3_n_Se_r3pita.bat";
}
