#coding:utf-8
#！/usr/bin/python
from mininet.topo import Topo
class Ring( Topo ):

    def __init__( self ):
        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Switchs = list()
        Hosts = list()
        for i in range(0,8):
            Switchs.append(self.addSwitch( 's'+str(i) ))
        
        for i in range(0,16):
            Hosts.append(self.addHost( 'h'+str(i) ))

        # Add links
        c = 0
        for i in range(0,8):
            self.addLink( Switchs[i], Switchs[(i+1)%8])
            self.addLink( Switchs[i], Hosts[c])
            c+=1
            self.addLink( Switchs[i], Hosts[c])
            c+=1
        
topos = { 'mytopo': ( lambda: MyTopo() ) }

if __name__ == '__main__':
    from onosnet import run
    run(Ring())
