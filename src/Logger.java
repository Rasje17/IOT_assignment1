abstract class Logger extends Thread {
    String filename;
    
    public Logger (String filename) {
        this.filename = filename;
    }
}
