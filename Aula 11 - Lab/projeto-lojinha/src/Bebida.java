public class Bebida extends Produto {
   private final int volume; 
   private final EnumAlergias alergia;
   private final EnumTemperaturasBebidas temperatura;
   private final EnumTiposBebida tipo;

    // Construtor
    public Bebida(double preco, int quantidade, String descricao, String nome, int volume, EnumAlergias alergia,
            EnumTemperaturasBebidas temperatura, EnumTiposBebida tipo) {
        super(preco, quantidade, descricao, nome);
        this.volume = volume;
        this.alergia = alergia;
        this.temperatura = temperatura;
        this.tipo = tipo;
    }

    // Getters e Setters
    public int getVolume() {
        return volume;
    }

    public EnumAlergias getAlergia() {
        return alergia;
    }

    public EnumTemperaturasBebidas getTemperatura() {
        return temperatura;
    }

    public EnumTiposBebida getTipo() {
        return tipo;
    }

    // Preco com desconto
    @Override
    public double gerarPrecoComDesconto() {
        return getPreco() * 0.9;
    }
}
