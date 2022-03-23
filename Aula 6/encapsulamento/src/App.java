public class App {
    public static void main(String[] args) throws Exception {

        Cliente c1 = new Cliente("Felippe",
            "123456789",
            "Felippe.onishi@gmail.com",
             new Conta(1234)
        );

        System.out.println("Nome do cliente: " +c1.getNome());
        System.out.println("E-mail do cliente: " +c1.getEmail());
        System.out.println("CPF do cliente: " +c1.getCpf());
        c1.getConta().visualizarSaldo();
    }
}
