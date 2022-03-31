
public class Contas {
    private double idConta;
    private double saldo;
    private Usuarios usuario;

    // Construtor
    public Contas(double idConta, double saldo, Usuarios usuario){
    this.idConta = Math.random();
    this.saldo = saldo;
    this.usuario = usuario;
    }

    public void visualizarConta(){
    System.out.println("ID da conta: "+ idConta);
    System.out.println("Usuario: "+ usuario);
    }

    public String visualizarSaldo(){
        return String.format("Saldo da conta: R$%.2f", saldo);
        
    }



    public boolean depositar(double valor){
        if(valor < 0) 
            return false;
        this.saldo += valor;
        return true;
    }
    public boolean sacar(double valor){
        if(valor > saldo) return false;
        if(valor < 0) return false;
        this.saldo -= valor;
        return true;
    }
//     public boolean transferirDinheiro(double valor, idConta destino){
//         if(!sacar(valor)) return false;
//         if(!destino.depositar(valor)) return false;
//         return true;
//     }

//     public String toString(){
//         return "ID da conta:"+ usuario.idConta();
//         + "\nCliente:" + usuario.getNome()
//         + "\nSaldo:" + visualizarSaldo();
//     }
// }   



    }


















