public class Comida extends Produto{
    private final String origem;
    private final double peso;
    private final EnumAlergias alergia;
    private final EnumTiposComida tipo;

    // Construtor
    public Comida(double preco, int quantidade, String descricao, String nome, String origem, double peso,
            EnumAlergias alergia, EnumTiposComida tipo) {
        super(preco, quantidade, descricao, nome);
        this.origem = origem;
        this.peso = peso;
        this.alergia = alergia;
        this.tipo = tipo;
    }

    // Getters e Setters
    public String getOrigem() {
        return origem;
    }

    public double getPeso() {
        return peso;
    }

    public EnumAlergias getAlergia() {
        return alergia;
    }

    public EnumTiposComida getTipo() {
        return tipo;
    }

    // Preco com desconto
    @Override
    public double gerarPrecoComDesconto() {
        return getPreco() * 0.95;
    }
}
