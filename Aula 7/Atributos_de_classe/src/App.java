public class App {
    public static void main(String[] args) throws Exception {
        // System.out.println("Valor do contador: "+ Exemplo.getContador() + "\n");
        // Exemplo e1 = new Exemplo("Goku", 8001);
        // Exemplo e2 = new Exemplo("Vegeta", 8000);
        // System.out.println(e1);
        // System.out.println(e2);
        // System.out.println("Valor do contador: "+ Exemplo.getContador());
        System.out.println("" + ValidadorCPF.validar("11111111111"));
        System.out.println("" + ValidadorCPF.validar("11111111112"));
        System.out.println("" + ValidadorCPF.validar("52998224725"));
        System.out.println("" + ValidadorCPF.validar("52998224735"));
        System.out.println("" + ValidadorCPF.validar("52998224726"));
        System.out.println("" + ValidadorCPF.validar("50961364858"));
        System.out.println("" + ValidadorCPF.validar("50958"));
        System.out.println("" + ValidadorCPF.validar("509.613.648-58"));
        System.out.println("" + ValidadorCPF.validar("095.382.418-78"));
    
    }
}
