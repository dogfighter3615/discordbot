package discordchats.discordchat.util;
import discordchats.discordchat.Discordchat;
import net.minecraft.entity.player.PlayerEntity;
import net.minecraft.network.message.MessageType;
import net.minecraft.network.message.SentMessage;
import net.minecraft.server.MinecraftServer;
import net.minecraft.server.network.ServerPlayerEntity;
import net.minecraft.text.LiteralTextContent;
import net.minecraft.text.Text;
import org.apache.logging.log4j.core.jmx.Server;
import net.minecraft.text.Style;

public class sendchat  {

    public static void message(Text msg, boolean broadcast,  ServerPlayerEntity player){
        if (!broadcast){
            player.sendMessage(msg,false);
        } else{
            for (ServerPlayerEntity player1 : Discordchat.server.getPlayerManager().getPlayerList()){
                player1.sendMessage(msg,false);
            }
        }
    }

    //public static void message(ServerPlayerEntity player, Text msg, boolean broadcast) {
    //    if (!broadcast) {
    //        player.sendSystemMessage(msg);
    //    } else {
    //        MinecraftServer server = player.getServer();
    //        if (server == null) {
    //            return; // Shouldn't happen
    //        }
//
    //        server.sendSystemMessage(msg);
    //        for (ServerPlayerEntity player1 : server.getPlayerManager().getPlayerList()) {
    //            player1.sendSystemMessage(msg);
    //        }
    //    }
    //}
}
