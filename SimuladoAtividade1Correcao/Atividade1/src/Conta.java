public class Conta {
    private int idConta;
    private double saldo;
    private static int totalContas = 0;

    // Construtor
    public Conta() {
        this.saldo = 0;
        this.idConta = totalContas;
        totalContas++;
    }

    // Depositar
    public boolean depositar(double valor){
        this.saldo += valor;
        return true;
    }

    // Sacar
    public boolean sacar(double valor){
        if(valor > this.saldo)
            return false;
        this.saldo -= valor;
        return true;
    }

    // Transferir
    public boolean transferir(double valor, Conta destino){
        if(!sacar(valor))
            return false;
        return destino.depositar(valor);
    }

    // Getter
    public int getIdConta() {
        return idConta;
    }

    public double getSaldo() {
        return saldo;
    }

    // toString
    @Override
    public String toString() {
        return "Conta [idConta=" + idConta + ", saldo=" + saldo + "]";
    }


}
