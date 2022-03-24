public class Cliente {
    private String cpf;
    private String nome;
    private String email;


    public Cliente(String nome, String cpf, String email){
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
    
    }

    public void visualizarCliente(){
        System.out.println("Dados do Cliente:");
        System.out.println("Nome: "+ nome);
        System.out.println("CPF: "+ cpf);
        System.out.println("E-mail: "+ email);
    
    }

    // Pegar nome
    public String getNome(){
        return nome;
    }

    // Setar nome
    public void setNome(String nome){
        this.nome = nome;
    }

    // Pegar cpf
    public String getCpf(){
        return cpf;
    }

    // Pegar email
    public String getEmail(){
        return email;
    }

    // Setar email
    public void setEmail(String email){
        this.email = email;
    }
}
