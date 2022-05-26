public class Literatura extends Produto{
    private final String editora;
    private final String autor;
    private final int paginas;
    private final EnumGeneroLiteratura genero;

    // Construtor
    public Literatura(double preco, int quantidade, String descricao, String nome, String editora, String autor,
            int paginas, EnumGeneroLiteratura genero) {
        super(preco, quantidade, descricao, nome);
        this.editora = editora;
        this.autor = autor;
        this.paginas = paginas;
        this.genero = genero;
    }

    // Getters e Setters
    public String getEditora() {
        return editora;
    }

    public String getAutor() {
        return autor;
    }

    public int getPaginas() {
        return paginas;
    }

    public EnumGeneroLiteratura getGenero() {
        return genero;
    }

    // Preco com desconto
    @Override
    public double gerarPrecoComDesconto() {
        return getPreco();
    }
}
