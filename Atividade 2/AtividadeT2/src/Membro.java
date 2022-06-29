public abstract class Membro implements IPostarMensagem {
    private String userName;
    private String email;
    private EnumFuncao funcao;
    private EnumHorarios horario;
    private String regularMessage;
    private String extraMessage;


    public Membro(String userName, String email, EnumFuncao funcao, EnumHorarios horario) {
        this.userName = userName;
        this.email = email;
        this.funcao = funcao;
        this.horario = horario;
    }



    public String getUserName() {
        return userName;
    }



    public void setUserName(String userName) {
        this.userName = userName;
    }



    public String getEmail() {
        return email;
    }



    public void setEmail(String email) {
        this.email = email;
    }



    public EnumFuncao getFuncao() {
        return funcao;
    }



    public void setFuncao(EnumFuncao funcao) {
        this.funcao = funcao;
    }



    public EnumHorarios getHorario() {
        return horario;
    }



    public void setHorario(EnumHorarios horario) {
        this.horario = horario;
    }

    public String getRegularMessage() {
        return regularMessage;
    }



    public void setRegularMessage(String regularMessage) {
        this.regularMessage = regularMessage;
    } 


    public String getExtraMessage() {
        return extraMessage;
    }


    public void setExtraMessage(String extraMessage) {
        this.extraMessage = extraMessage;
    }


    public void PostarMensagem(){
        if(this.getHorario().equals(EnumHorarios.REGULAR)){
            System.out.println("Membro: "+ getUserName()+ " Função: "+getFuncao()+ " Mensagem: "+getRegularMessage());
        }else{
            System.out.println("Membro: "+ getUserName()+ " Função: "+getFuncao()+" Mensagem: "+getExtraMessage());
        }
    }

}