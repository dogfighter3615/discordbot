package discordchats.discordchat.client;

import jdk.jfr.EventFactory;
import net.fabricmc.api.ClientModInitializer;
import net.fabricmc.api.EnvType;
import net.fabricmc.api.Environment;
import java.awt.Desktop;
import java.io.*;

@Environment(EnvType.CLIENT)
public class DiscordchatClient implements ClientModInitializer {
    @Override
    public void onInitializeClient() {
    //    File file = new File("C:\\Users\\david\\IdeaProjects\\discord_chat\\src\\main\\java\\discordchats\\discordchat\\client\\bot.txt");
    //    Desktop desktop = Desktop.getDesktop();
    //    desktop.open(file);
    }

}

//public final class ServerSendPackage {
//    private static final Logger LOGGER = logmanager.
//}