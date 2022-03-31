public class Usuarios {
    private String nome;
    private String senha;
    private String email;
    

    // Construtor
    public Usuarios(String nome, String senha, String email){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
    }
    

    public void visualizarUsuario(){
        System.out.println("Dados do usuario:");
        System.out.println("Nome: "+ nome);
        System.out.println("Senha: "+ senha);
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
    
    // Pegar senha
    public String getSenha(){
        return senha;
    }

    // Setar senha
    public void setSenha(String senha){
        this.senha = senha;
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

