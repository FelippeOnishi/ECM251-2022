public class Exemplo{
    private String texto;
    private double valor;
    public static int contador = 0;

    public Exemplo(String texto, double valor){
        this.texto = texto;
        this.valor = valor;
        contador += 1;
    }

    public String toString(){
        return "Texto: " + this.texto
        + "\nValor: " + this.valor 
        + "\nContador: "+ contador + "\n";
    }

    public static int getContador(){
        return contador;
    }
}