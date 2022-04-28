public class Sistema {

    public static void executar(){
        Carro c1 = new Carro(2000, "Audi");
        Carro c2 = new Carro(2500, "BMW");
        Bicicleta b1 = new Bicicleta(250, "Caloi");
        Moto m1 = new Moto(500, "Honda");

        Usuario usuario1 = new Usuario("Felippe");
        Usuario usuario2 = new Usuario("Ahmad");
        Usuario usuario3 = new Usuario("Caio");
        Usuario usuario4 = new Usuario("Lucas");

        System.out.println("---------- Aluguel 1 ---------- ");
        usuario1.alugar(c2);
        System.out.println(c2);
        System.out.println(usuario1);

        System.out.println("---------- Aluguel 2 ---------- ");
        usuario2.alugar(m1);
        System.out.println(m1);
        System.out.println(usuario2);

        System.out.println("---------- Aluguel 3 ---------- ");
        usuario3.alugar(c1);
        System.out.println(c1);
        System.out.println(usuario3);

        System.out.println("---------- Aluguel 4 ---------- ");
        usuario4.alugar(b1);
        System.out.println(b1);
        System.out.println(usuario4);
    }

}
