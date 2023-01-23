package discordchats.discordchat.network.events;
import discordchats.discordchat.network.SendPacket;
import discordchats.discordchat.network.MakeConnection;
import discordchats.discordchat.Discordchat;
import discordchats.discordchat.network.connect;
import net.fabricmc.fabric.api.message.v1.ServerMessageEvents;
import net.minecraft.network.message.MessageType;
import net.minecraft.network.message.SignedMessage;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.Style;
import java.io.IOException;
import java.net.SocketException;

import discordchats.discordchat.network.SendPacket;
public class messagehandler implements ServerMessageEvents.ChatMessage {

    @Override
    public void onChatMessage(SignedMessage message, ServerPlayerEntity sender, MessageType.Parameters params) {
        Discordchat.LOGGER.info(message.signedBody().content().plain());
        //Discordchat.LOGGER.info(sender.getServer().toString());
        //Discordchat.LOGGER.info(String.valueOf(message.signedBody().content().decorated().getStyle()));
        if (message.signedBody().content().plain().equals("restart")){
            Discordchat.LOGGER.info("weeeeeeeeaaeaeaeaeaaaaaaaaaaaaaaaaaaaaaaa");
            connect.stop = true;
            try {
                Thread.sleep(1000);
                Discordchat.LOGGER.info("waited");
                connect.main();
            } catch (InterruptedException e) {
                Discordchat.LOGGER.info(e.toString());
            }
        } else{
        try {
            connect.send(message.signedBody().content().plain(),false);
        } catch (IOException e) {
            Discordchat.LOGGER.info(e.toString());
        }
    }}
}
