#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <dirent.h>
#include <pthread.h> //pthread 헤더
#define SERV_IP "220.149.128.103" 
#define SERV_PORT 4539
pthread_t chatview;//채팅을 출력 위해 만든 쓰레드
pthread_t chatwrite;//채팅을 입력해 서버로 전송하기 위해 만든 쓰레드
char sendmessage[100]; //3번 문제에서 서버에서 받은 포트와 IP의 정보값
struct flag { //플래그를 구조체로 생성하였다.
	int sockfd; //소켓
	int rcv_byte; 
	int writeFlag; //클라이언트 화면에 출력하는 플래그 
	int exitFlag; //클라이언트 종료 플래그
};
struct flag c;
int recv_t(int socket, char* buf, int buff, int i) {//흐름 보기 위해 만든 함수
	int t;
	t = recv(socket, buf, buff, 0);
	return t;
}
int send_t(int socket, char* buf, int buff, int i) {//흐름 보기 위해 만든 함수
	int t;
	t = send(socket, buf, buff, 0);
	if (t > -1) {
		//printf("send : %d, %d\n", i,t);
	}
	return t;
}
void* chatview_thread(void* argu) { // 쓰레드 chatview가 실행하는 함수
	char recvBuf[512];
	while (1) {
		c.rcv_byte = recv_t(c.sockfd, recvBuf, 512, 12);
		if (c.rcv_byte > -1) { //받으면
			if (c.writeFlag == 0) { //자신이 보낸 채팅이 아니면
				printf("%s", recvBuf); //출력
			}
			else {
				c.writeFlag = 0;
			}
		}
		if (c.exitFlag == 1) { //종료 플래그가 1이면
			//printf("bye");
			pthread_exit(NULL); //쓰레드 종료
		}
	}
	return NULL;
}
void* chatwrite_thread(void* argu) { //쓰레드 chatwrite가 실행하는 함수
	char buf[512];
	int t;
	int index = 0;
	char message[512];
	strcpy(message, "");
	while (1) {
		//printf("message: %s",message);
		fgets(message, sizeof(message), stdin); // 메시지를 입력받음
		c.writeFlag = 1; //입력한 메시지가 있으면 자신이 보냈다는 것을 알기 위해 writeflag를 1로 변경해서 
		t = send_t(c.sockfd, message, sizeof(message), 13); //서버로 전송
		if (strcmp(message, ":q\n") == 0) { //:q를 치면
			//printf("bye");
			c.exitFlag = 1; //exitFlag 1로 ??捐?
			strcpy(message, "");
			pthread_exit(NULL); //쓰레드 종료
		}
		//}
	}
	return NULL;
}
int main(int argc, char* argv[]) {
	struct sockaddr_in dest_addr;
	char buf[512];
	char buf2[512];
	char id[20];
	char pw[20];
	char chatReceive[512];
	c.writeFlag = 0;
	c.exitFlag = 0;
	c.sockfd = socket(AF_INET, SOCK_STREAM, 0);
	c.exitFlag = 0;
	if (c.sockfd == -1)
	{
		perror("client-socket() error lol!");
		exit(1);
	}
	else printf("client-socket() sockfd is OK...\n");
	dest_addr.sin_family = AF_INET;
	dest_addr.sin_port = htons(SERV_PORT);
	dest_addr.sin_addr.s_addr = inet_addr(SERV_IP);

	memset(&(dest_addr.sin_zero), 0, 8);

	if (connect(c.sockfd, (struct sockaddr*) & dest_addr, sizeof(struct sockaddr)) == -1) {
		perror("client-connect() error lol");
		exit(1);
	}
	else printf("client-connect() is ok...\n");
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 1);// i = 1 서버에서 환영하는 메시지 받음 
	printf("%s\n", buf);
	printf("id: ");
	scanf("%s", id);
	send_t(c.sockfd, id, strlen(id) + 1, 2);//i = 2 id를 전송
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 3);//i = 3 확인 받음
	printf("pw: ");
	scanf("%s", pw);
	send_t(c.sockfd, pw, strlen(pw) + 1, 4);//i = 4 pw를 전송
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 5);//i = 5 서버에서  로그인 메시지 받음
	printf("buf :%s\n", buf); //로그인 메시지 출력
	send_t(c.sockfd, "ack", 4, 6);//i = 6 로그인 완료 확인 신호를 보냄 
	//port
	strcpy(buf, "");
	printf("buf: %s\n", buf);
	c.rcv_byte = recv_t(c.sockfd, buf, sizeof(buf), 7);//7 로그인 서버에서 확인 신호를 받음
	printf("buf: %s\n", buf);
	send_t(c.sockfd, "ack", 4, 8);//분기 2, i = 8
	//chat
	c.rcv_byte = recv_t(c.sockfd, buf2, sizeof(buf2), 11);//분기 1일땐 i = 9, 분기 2일땐 i = 9
	printf("buf: %s\n", buf2);
	if (strcmp(buf2, "chat") == 0) { //buf2가 
		printf("---------------Chatting Room---------------\n");
		pthread_create(&chatview, NULL, &chatview_thread, NULL); //채팅 쓰레드 생성
		pthread_create(&chatwrite, NULL, &chatwrite_thread, NULL); 
		pthread_join(chatwrite, NULL);// :q 눌려서 쓰레드 끝날때까지 대기
		pthread_join(chatview, NULL);
	}
	//printf("exit %d", c.exitFlag);
	close(c.sockfd); //:q눌리면 소켓을 닫고
	exit(0); // 프로세스 종료
}

