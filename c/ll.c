#include <stdio.h>

typedef struct node {
    int val;
    struct node *next;
} firstNode;

int main(int argc, int *argv[]) {
    struct node firstNode;
    firstNode.val = 1;
    struct node nextNode;
    firstNode.next = &nextNode;
    nextNode.val = firstNode.val + 1;
    /* DEBUG
    if (nextNode.next == NULL) {
        printf("next passed\n");
    } else {
        printf("did not pass\n");
    }
    */

    int count = 0;
    struct node curr = firstNode;
    printf("currNode value %i\n", curr.val);
    if (curr.next == &nextNode) {
        printf("it's null, wtf");
    }
    while(curr.next != NULL) {
        count++;
        curr = *curr.next;
        printf("%i", curr.val);
    }
    int ll[count - 1];
    printf("%i", ll[0]);
    count = 0;
    curr = firstNode;
    printf("second currNode value %i\n", curr.val);
    while(curr.next != NULL) {
        ll[count++] = curr.val;
        curr = *curr.next;
    }
    int i;
    for(i = count; i > 0; i--) {
        printf("Printing reversed linked list");
        printf("======");
        printf("%i element is %i", i, ll[i]);
        printf("======");
    }
}

