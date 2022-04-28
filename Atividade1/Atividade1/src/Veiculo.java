import java.util.concurrent.ThreadLocalRandom;

public class Veiculo {
    private String tipo;
    protected int id;
    private int Preco;

    // Construtor
    public Veiculo(int Preco, String tipo) {
        this.Preco = Preco;
        this.tipo = tipo;
        GerarID();
    }

    public int getPreco() {
        return Preco;
    }

    public String getTipo() {
        return tipo;
    }

    // Funcao Testar
    public void testar(){
        System.out.println("ID: "+ id + ", custo de aluguel por hora: "+ Preco);
    }

    // Funcao para gerar ID aleatorio
    public void GerarID(){
        this.id = ThreadLocalRandom.current().nextInt(10000,100000);
    }


    // toString
    @Override
    public String toString() {
        return "Veiculo [Preco=" + Preco + ", id=" + id + ", tipo=" + tipo + "]";
    }


}
