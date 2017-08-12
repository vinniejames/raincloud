import subprocess
import playlist

songs = playlist.songs

for song in songs:
    print song
    subprocess.call("youtube-dl " + song, shell=True)

print """
            ------               _____
           /      \ ___\     ___/    ___
        --/-  ___  /    \/  /  /    /   \
       /     /           \__     //_     \
      /                     \   / ___     |
      |           ___       \/+--/        /
       \__           \       \           /
          \__                 |          /
         \     /____      /  /       |   /
          _____/         ___       \/  /\
               \__      /      /    |    |
             /    \____/   \       /   //
         // / / // / /\    /-_-/\//-__-
          /  /  // /   \__// / / /  //
         //   / /   //   /  // / // /
          /// // / /   /  //  / //
       //   //       //  /  // / /
         / / / / /     /  /    /
      ///  / / /  //  // /  // //
         ///    /    /    / / / /
    ///  /    // / /  // / / /  /
       // ///   /      /// / /
      /        /    // ///  /

Enjoy :P
"""
