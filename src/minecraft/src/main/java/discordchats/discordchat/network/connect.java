package discordchats.discordchat.network;


import discordchats.discordchat.Discordchat;
import discordchats.discordchat.util.sendchat;
import net.minecraft.text.Text;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.nio.charset.StandardCharsets;
import java.util.Objects;

public class connect extends Thread {
    public static boolean stop = false;
    public static Socket socket;
    public static int port = 25585;
    private static boolean hold;
    public static String packet;
    private static String message;
    public static boolean connected;
    public static void main(){
        stop = false;
        hold = false;
        connect thread = new connect();
        Discordchat.LOGGER.info("hello");
        thread.start();
    }

    public void run(){
        try{


            ServerSocket serversocket = new ServerSocket(port);

            while(!stop){

                Discordchat.LOGGER.info(String.valueOf(stop));
                socket = serversocket.accept();
                connected = true;
                InputStream is = socket.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                BufferedReader br = new BufferedReader(isr);
                //Discordchat.LOGGER.info(br.readLine());
                message = br.readLine();

                if(Objects.equals(message, "stop")){
                    stop = true;
                    Discordchat.LOGGER.info(String.valueOf(stop));
                    Discordchat.LOGGER.info("weeeeeeeeeeeaaaa");
                }

                Discordchat.LOGGER.info(message);

                Discordchat.LOGGER.info(stringtotext(message).toString());
                sendchat.message(stringtotext(message),true,null);
            }
            Discordchat.LOGGER.info("waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
        } catch (SocketException e){
            try {
                try{
                    socket.close();

                } catch (NullPointerException eeeeee){
                    Discordchat.LOGGER.info(eeeeee.toString());
                }
            } catch (IOException ex) {
                Discordchat.LOGGER.info(ex.toString()+"1");
            }
        } catch (IOException e) {
            Discordchat.LOGGER.info(e.toString()+"2");
        }
    connected = false;
    }
    public static void send(String string,boolean system) throws IOException {
         if (connected){
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            Discordchat.LOGGER.info(string+"reeeee");

            String sendstring = "";
            if (system){
                sendstring = string;
            }
            if(!system){
                sendstring = "p"+string;
            }
            byte[] bytes = sendstring.getBytes(StandardCharsets.UTF_8);
            Discordchat.LOGGER.info(String.valueOf(bytes));
            out.write(bytes);

            //out.writeUTF(sendstring);

            if (!hold) {
                out.flush();
            }
         }
    }

    private Text stringtotext(String message) {
        return Text.literal(message);
    }
}
