import java.util.ArrayList;

public class App {
    private static EnumHorarios horarioAtual = EnumHorarios.REGULAR;
    public static EnumHorarios getHorarioAtual(){
        return horarioAtual;
    }

    public static void setHorarioAtual(EnumHorarios horarioAtual){
        App.horarioAtual = horarioAtual;
    }

    public static void main(String[]args)throws Exception{
        System.out.println("Bem vindo ao sistema da MAsK_S0c13ty");



        ArrayList<Membro> AllMembers = new ArrayList<Membro>();
        AllMembers.add(new MobileMembers("Felippe", "Felippe123@gmail.com", EnumFuncao.MOBILEMEMBER, horarioAtual));
        AllMembers.add(new BigBrother("Joaozinho123", "Joaozinho321@gmail.com", EnumFuncao.BIGBROTHER, horarioAtual));
        AllMembers.add(new HeavyLift("Pedrinho987", "AcordaPedrinho@gmail.com", EnumFuncao.HEAVYLIFTER, horarioAtual));
        AllMembers.add(new ScriptGuy("Ahmad567", "Ahmad@gmail.com", EnumFuncao.SCRIPTGUY, horarioAtual));

        postarMensagem(AllMembers);

        mudarHorario(EnumHorarios.EXTRA, AllMembers);
        System.out.println(horarioAtual);

        postarMensagem(AllMembers);

        mudarHorario(EnumHorarios.REGULAR, AllMembers);
        System.out.println(horarioAtual); 

        removerMembro("Pedrinho987", AllMembers);
        removerMembro("Ahmad567", AllMembers);

        postarMensagem(AllMembers);

        System.out.println("Saindo do sistema.");
    }

    public static void mudarHorario(EnumHorarios horarios, ArrayList<Membro> AllMembers){
        setHorarioAtual(horarios);
        for (Membro member : AllMembers){
            member.setHorario(horarios);
        }
    }

    public static void postarMensagem(ArrayList<Membro> Allmembers){
        for(Membro member : Allmembers){
            member.PostarMensagem();
        }
    }

    public static void removerMembro(String userName, ArrayList<Membro> AllMembers){
        int i = 0;
        int remove_i = 0;
        for (Membro member : AllMembers){
            if(member.getUserName().equals(userName)){
                remove_i = i;
            }
            i++;
        }
        AllMembers.remove(remove_i);
    }
}
