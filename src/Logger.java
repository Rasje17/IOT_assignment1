import java.io.FileWriter;
import java.io.IOException;

abstract class Logger extends Thread {
    String filename;
    FileWriter writer;
    String separator;
    
    protected Logger (String filename, String separator) throws IOException {
        this.filename  = filename;
        this.separator = separator;
        this.writer = new FileWriter(filename);
        writer.write("# timestamp"+separator+"entry"+System.lineSeparator());
    }
    
    protected void log (String line) throws IOException {
        writer.write(System.currentTimeMillis()+separator+line+System.lineSeparator());
    }
    
    protected void finalize () throws IOException {
        writer.close();
    }
}
