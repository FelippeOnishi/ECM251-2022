public class Genin extends Ninja {
    public Genin(String name, String family, String[] jutsus, String mission) {
        super(name, family, jutsus);
        this.mission = mission;
    }

    private String mission;

    public String goToMission(){
        return String.format("%s está indo na missao %s", getName(), mission);
    }

    @Override
    public String train(){
        return String.format("%s está treinandoo jutsu %s!", getName(), getJutsus()[0]);
    }

}


//  Consegui arrumar la o problema, na hora que voce caiu eu rodei o amazon corretto dnv e reiniciei o pc kkkk