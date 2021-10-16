from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.link import Link, TCLink
from mininet.net import Mininet

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1', mac = '00:00:00:00:00:01')
        h2 = self.addHost( 'h2', mac = '00:00:00:00:00:02')
        h3 = self.addHost( 'h3', mac = '00:00:00:00:00:03')
        h4 = self.addHost( 'h4', mac = '00:00:00:00:00:04')
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )



        # Add links
        self.addLink( h1, s1, bw=20,delay='100ms', loss=0)
        self.addLink( h2, s2, bw=20,delay='100ms', loss=0)
        self.addLink( h3, s3, bw=20,delay='100ms', loss=0)
        self.addLink( h4, s4, bw=20,delay='100ms', loss=0)
        self.addLink( s1, s5, bw=5, delay='100ms', loss=10)
        self.addLink( s5, s2, bw=5, delay='100ms', loss=10)
        self.addLink( s2, s3, bw=8, delay='100ms', loss=10)
        self.addLink( s3, s4, bw=8, delay='100ms', loss=10)
        self.addLink( s4, s1, bw=8, delay='100ms', loss=10)



topos = { 'mytopo': ( lambda: MyTopo() ) }
