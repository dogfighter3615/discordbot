package discordchats.discordchat.network;

import discordchats.discordchat.Discordchat;
import discordchats.discordchat.network.SendPacket;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.BindException;
import java.net.ServerSocket;
import java.net.Socket;
import javax.swing.JOptionPane;
import java.net.SocketTimeoutException;
public class MakeConnection {
    public static Socket sock;
    public static DataOutputStream out;

    public static ServerSocket serverSock;
    public static void connect()throws java.io.IOException {

        ServerSocket serverSock = new ServerSocket(25585);
        serverSock.setSoTimeout(10000);


        try {
            Discordchat.LOGGER.info("weeeeeeeeeeee");
            sock = serverSock.accept();
            out = new DataOutputStream(sock.getOutputStream());


        } catch (SocketTimeoutException e) {
            Discordchat.LOGGER.info(e.toString());
        } catch (BindException e){
            sock.close();
            Discordchat.LOGGER.info("weeeeeeeeeeee");
            sock = serverSock.accept();
            out = new DataOutputStream(sock.getOutputStream());
        }
    }

    public static void SendPacket(String text) throws IOException{
            out = new DataOutputStream((sock.getOutputStream()));
            out.writeChars(text);
            sock.close();
            connect();


        }
        //int Port = Integer.parseInt("25585");
        //String IP = "127.0.0.1";
        //ServerSocket serverSock = new ServerSocket(25585);
        //Socket Sock = serverSock.accept();


        //DataInputStream in = new DataInputStream(Sock.getInputStream());
        //Discordchat.LOGGER.info(in.readUTF());
        //Sock.close();


}