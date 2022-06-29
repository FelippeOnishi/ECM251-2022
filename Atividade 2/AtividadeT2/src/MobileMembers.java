public class MobileMembers extends Membro{

    public MobileMembers(String userName, String email, EnumFuncao funcao, EnumHorarios horario) {
        super(userName, email, funcao, horario);

        setRegularMessage(regularMessage);
        setExtraMessage(extraMessage);

    }
    
    private final String regularMessage = "Happy Coding!";
    private final String extraMessage = "MAsK_S0c13ty";    
    
}
