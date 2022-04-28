public class Usuario {
    private String nome;
    private Veiculo veiculo;

    // Construtor
    public Usuario(String nome) {
        this.nome = nome;
    }


    // Setter e Getter
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }


    public Veiculo getVeiculo() {
        return veiculo;
    }


    public void setVeiculo(Veiculo veiculo) {
        this.veiculo = veiculo;
    }


    @Override
    public String toString() {
        return "Usuario [nome=" + nome + "]";
    }



    public void alugar(Veiculo veiculo){
        setVeiculo(veiculo);
    }
    
    
}
