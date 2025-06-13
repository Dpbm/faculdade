import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { bootstrapApplication } from '@angular/platform-browser';
import { Card } from './app/card/card.component';

type CardData = {
  title: string;
  subtitle: string;
};

@Component({
  selector: 'app-root',
  templateUrl: 'main.html',
  imports: [CommonModule, Card],
  styleUrl: './main.css',
})
export class PlaygroundComponent {
  data: CardData[] = [
    { title: 'test', subtitle: 'test' },
    { title: 'test', subtitle: 'test' },
    { title: 'test', subtitle: 'test' },
    { title: 'test', subtitle: 'test' },
    { title: 'test', subtitle: 'test' },
    { title: 'test', subtitle: 'test' },
  ];
}

bootstrapApplication(PlaygroundComponent);
