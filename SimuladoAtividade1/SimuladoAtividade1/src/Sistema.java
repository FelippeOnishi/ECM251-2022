public class Sistema {
    public void run(){

        Usuarios u1 = new Usuarios("Felippe","12345", "Felippe.onishi@gmail.com");
        Contas c1 = new Contas(1,1000, u1);
        u1.visualizarUsuario();
        c1.visualizarConta();
        System.out.println(c1.visualizarSaldo());
        System.out.println("\n");

        Usuarios u2 = new Usuarios("Ahmad", "123", "Ahmad@gmail.com");
        Contas c2 = new Contas(2, 250, u2);
        u2.visualizarUsuario();
        c2.visualizarConta();
        System.out.println(c2.visualizarSaldo());
        System.out.println("\n");

        Usuarios u3 = new Usuarios("Michelle","1234", "Michelle@gmail.com");
        Contas c3 = new Contas(1,3000, u3);
        u3.visualizarUsuario();
        c3.visualizarConta();
        System.out.println(c3.visualizarSaldo());
        System.out.println("\n");
    }
}