public class BigBrother extends Membro{

    public BigBrother(String userName, String email, EnumFuncao funcao, EnumHorarios horario) {
        super(userName, email, funcao, horario);

        setRegularMessage(regularMessage);
        setExtraMessage(extraMessage);

    }

    private final String regularMessage = "Sempre ajudando as pessoas membros ou não S2!";
    private final String extraMessage = "..."; 

}