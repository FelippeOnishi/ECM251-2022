public class App {
    public static void main(String[] args) throws Exception {
        // Cria duas referencias para objetos do tipo configuracao
        Configuracao c1;
        Configuracao c2;
        // Cria as instancias
        c1 = new ConfiguracaoDesenvolvimento("localhost", "localhost:5000");
        c2 = new ConfiguracaoProducao("http://aws.meubanco.com", "https://mnhamaua.br", "Jorge");
        System.out.println("conf1: "+ c1);
        System.out.println("Conf2: "+ c2);

        // Verificacao de usuarios
        System.out.println(c1.getUser());
        System.out.println(c2.getUser());
    }
}
