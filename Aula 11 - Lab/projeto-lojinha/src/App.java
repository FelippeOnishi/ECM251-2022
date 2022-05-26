public class App {
    public static void main(String[] args) throws Exception {
        Produto manga = new Literatura(29.90, 10, "Foda pa baralho", "Gantz", "JDBC", "Alguem", 100, EnumGeneroLiteratura.ENGENHARIA);
        Produto coca = new Bebida(6.0, 8, "Presente dos deuses", "Coca-Cola", 350, EnumAlergias.GLUTEN, EnumTemperaturasBebidas.FRIO, EnumTiposBebida.REFRIGERANTE);
        Produto teppoki = new Comida(24.50, 10, "Nhoque de Arroz", "Teppoki", "Coreano", 0.5, EnumAlergias.GLUTEN, EnumTiposComida.APIMENTADA);

        System.out.println("Precos Regulares: ");
        System.out.println(manga.getNome() + " R$"+ manga.getPreco());
        System.out.println(coca.getNome()+ " R$"+ coca.getPreco());
        System.out.println(teppoki.getNome()+ " R$"+ teppoki.getPreco());
        System.out.println("----------------------------||----------------------------");
        System.out.println("Precos com Desconto: ");
        System.out.println(manga.getNome()+ getPrecoComDesconto(manga));
        System.out.println(coca.getNome()+ getPrecoComDesconto(coca));
        System.out.println(teppoki.getNome()+ getPrecoComDesconto(teppoki));

    }

    public static String getPrecoComDesconto(IGerarDesconto produto){
        return " R$"+ produto.gerarPrecoComDesconto();
    }
}
