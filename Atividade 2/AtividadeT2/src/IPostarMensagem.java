public interface IPostarMensagem {
    public static String postarMensagem(Membro member){
        if(member.getHorario().equals(EnumHorarios.REGULAR)){
            System.out.println(member.getRegularMessage());
            return member.getRegularMessage();
        }else{
            System.out.println(member.getExtraMessage());
            return member.getExtraMessage();
        }

    }
}
