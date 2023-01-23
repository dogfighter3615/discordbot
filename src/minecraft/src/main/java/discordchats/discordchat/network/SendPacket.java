package discordchats.discordchat.network;

import discordchats.discordchat.Discordchat;

import java.io.DataOutputStream;
import java.io.IOException;

public class SendPacket {


    public static void SendPacket(String text) throws IOException {
        MakeConnection.out.writeChars(text);
        Discordchat.LOGGER.info("thru sendpacket");
        Discordchat.LOGGER.info(text);
    }

}
