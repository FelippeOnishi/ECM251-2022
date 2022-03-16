public class Caneta{
    // Características da caneta - seus atributos
    String modelo;
    String cor;
    double ponta;
    int carga;
    final int CARGA_MAXIMA = 100;
    boolean tampa;

    // Comportamento da caneta - seus métodos
    // for e if é para verificar se a caneta tem carga, caso não tenha avisar que está sem carga
    void escrever(String texto){
        for(int i = 0; i < texto.length(); i++){
            if (tampa = false){
                if(carga > 0 ){
                    System.out.print(texto.charAt(i));
                    carga -= 1;
                }
                }else {
                    System.out.println("\nCANETA SEM CARGA");
                    break;
                }
            else{
                System.out.println("CANETA TAMPADA");
                }
            }
            }
        }
        System.out.println();
    }
    // Seta os atributos nas repectivas canetas
    void iniciarCaneta(String modelo, String cor, double ponta, boolean tampa){
        this.modelo = modelo;
        this.cor = cor;
        this.ponta = ponta;
        this.carga = CARGA_MAXIMA;
        this.tampa = tampa;
    }
    
    // Função para pegar os dados das canetas e usar no println() [Não utilizamos pois é melhor usar o debuger caso queira verificar os status da caneta antes/depois de ser utilizada]
    // String pegarDados(){
    //     return "Modelo:" + modelo +
    //     "\nCor:" + cor +
    //     "\nPonta:" + ponta +
    //     "\nCarga:" + carga;
}
