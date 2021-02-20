import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class OutputLogger extends Logger {
    BufferedReader input;
    
    public OutputLogger (String filename, Process p) {
        super(filename);
        input = new BufferedReader(new InputStreamReader(p.getInputStream()));
    }
    
    public void run () {
        try {
            String line;
            while ((line = input.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("OutputLogger("+filename+") caught exception: "+e);
        }
    }
}
