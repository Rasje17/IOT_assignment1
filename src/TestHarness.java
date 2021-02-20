import java.util.Arrays;
//import java.io.BufferedReader;
//import java.io.InputStreamReader;
import java.io.IOException;

class TestHarness {
    public static void main (String[] args) throws IOException {
        // args
        if (args.length<2) {
            System.out.println(args);
            System.out.println(args.length);
            System.out.println("Syntax: java TestHarness LOG_PREFIX COMMAND");
            System.out.println("        java TestHarness run42 ls -l");
            System.exit(1);
        }
        String prefix = args[0];
        String command = String.join(" ", Arrays.copyOfRange(args, 1, args.length));
        System.out.println("Prefix: "+prefix);
        System.out.println("Command: "+command);
        
        // start process
        Process p = Runtime.getRuntime().exec(command);
        
        // start loggers
        Logger logger_output = new OutputLogger(prefix+"_output.log", p);
        logger_output.start();
        
//        // read output
//        BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
//        String line;
//        while ((line = input.readLine()) != null) {
//            System.out.println(line);
//        }
    }
}
